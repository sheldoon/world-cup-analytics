with ranked as (
    select
        *,
        row_number() over (
            partition by player.id
            order by _FILE_NAME desc
        ) as rn
    from {{ source('world_cup', 'scorers_external') }}
)

select
    player.id as player_id,
    player.name as player_name,
    {{ translate_team_name('player.nationality') }} as player_nationality,
    player.section as player_position,
    player.dateOfBirth as player_date_of_birth,
    team.id as team_id,
    team.name as team_name,
    team.tla as team_code,
    playedMatches as played_matches,
    goals,
    assists,
    penalties
from ranked
where rn = 1