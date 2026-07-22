select
    team_id,
    team_name,
    team_short_name,
    country_code,
    count(player_id) as squad_size,
    round(avg(player_age),1) as avg_age,
    min(player_age) as youngest_player_age,
    max(player_age) as oldest_player_age,
    countif(player_position = 'Goalkeeper') as goalkeepers,
    countif(player_position = 'Defence') as defenders,
    countif(player_position = 'Midfield') as midfielders,
    countif(player_position = 'Offence') as forwards,
    countif(player_age < 23) as players_sub23,
    countif(player_age >= 30) as players_over30

from {{ref('stg_players')}}

group by
    team_id,
    team_name,
    team_short_name,
    country_code