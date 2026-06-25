select
    match_id,
    match_date,
    match_status,
    matchday,
    stage,
    match_group,
    home_team_id,
    home_team_name,
    home_team_code,
    away_team_id,
    away_team_name,
    away_team_code,
    winner,
    home_goals,
    away_goals,
    home_goals_ht,
    away_goals_ht,
    home_goals + away_goals as total_goals,
    case
        when winner = 'HOME_TEAM' then home_team_name
        when winner = 'AWAY_TEAM' then away_team_name
        when winner = 'DRAW' then 'Draw'
        else null
    end as winner_name,
    case
        when match_status = 'FINISHED' then true
        else false
    end as is_finished

from {{ref('stg_matches')}}