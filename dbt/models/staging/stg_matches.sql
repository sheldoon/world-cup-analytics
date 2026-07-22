with ranked as (
    select
        *,
        row_number() over (
            partition by id
            order by _FILE_NAME desc
        ) as rn
    from {{ source('world_cup', 'matches_external') }}
)

select
    id as match_id,
    utcDate as match_date,
    status as match_status,
    matchday,
    stage,
    JSON_VALUE(TO_JSON_STRING(t), '$.group') as match_group,
    homeTeam.id as home_team_id,
    {{ translate_team_name('homeTeam.name') }} as home_team_name,
    homeTeam.tla as home_team_code,
    awayTeam.id as away_team_id,
    {{ translate_team_name('awayTeam.name') }} as away_team_name,
    awayTeam.tla as away_team_code,
    score.winner as winner,
    CASE 
        WHEN score.duration = 'PENALTY_SHOOTOUT' 
        THEN score.fullTime.home - score.penalties.home
        ELSE score.fullTime.home
    END as home_goals,
    CASE 
        WHEN score.duration = 'PENALTY_SHOOTOUT' 
        THEN score.fullTime.away - score.penalties.away
        ELSE score.fullTime.away
    END as away_goals,
    score.halfTime.home as home_goals_ht,
    score.halfTime.away as away_goals_ht
from ranked t
where rn = 1