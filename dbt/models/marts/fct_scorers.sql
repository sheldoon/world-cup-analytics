select 
    s.player_id,
    s.player_name,
    s.player_nationality,
    s.player_position,
    s.player_date_of_birth,
    DATE_DIFF(CURRENT_DATE(), s.player_date_of_birth, YEAR) as player_age,
    s.team_id,
    s.team_name,
    s.team_code,
    s.played_matches,
    s.goals,
    s.assists,
    s.penalties,
    s.goals - COALESCE(s.penalties, 0) as open_play_goals,
    ROUND(s.goals / s.played_matches, 2) as goals_per_match

from {{ref('stg_scorers')}} s