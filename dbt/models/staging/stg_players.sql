with teams as (
    select
        *,
        row_number() over (
            partition by id
            order by _FILE_NAME desc
        ) as rn
    from {{ source('world_cup', 'teams_external') }}
),

latest_teams as (
    select * from teams where rn = 1
)

select
    t.id as team_id,
    {{ translate_team_name('t.name') }} as team_name,
    t.shortName as team_short_name,
    t.area.code as country_code,
    player.id as player_id,
    player.name as player_name,
    {{ translate_team_name('player.nationality') }} as player_nationality,
    player.position as player_position,
    player.dateOfBirth as player_date_of_birth,
    DATE_DIFF(CURRENT_DATE(), player.dateOfBirth, YEAR) as player_age
from latest_teams t,
UNNEST(t.squad) as player
where player.position != 'Coach'