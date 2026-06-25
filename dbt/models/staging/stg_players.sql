select
    team_id,
    team_name,
    team_short_name,
    country_code,
    player_id,
    player_name,
    player_nationality,
    player_position,
    player_date_of_birth,
    player_age

from {{ source('world_cup', 'players')}}