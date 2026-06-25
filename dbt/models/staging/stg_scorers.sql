select
    player_id,
    player_name,
    player_nationality,
    player_position,
    player_date_of_birth,
    team_id,
    team_name,
    team_code,
    playedMatches as played_matches,
    goals,
    assists,
    penalties

from {{source('world_cup', 'scorers')}}