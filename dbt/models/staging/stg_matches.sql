select
    id as match_id,
    utcDate as match_date,
    status as match_status,
    matchday,
    stage,
    `group` as match_group,
    homeTeam.id as home_team_id,
    homeTeam.name as home_team_name,
    homeTeam.tla as home_team_code,
    awayTeam.id as away_team_id,
    awayTeam.name as away_team_name,
    awayTeam.tla as away_team_code,
    score.winner as winner,
    score.fullTime.home as home_goals,
    score.fullTime.away as away_goals,
    score.halfTime.home as home_goals_ht,
    score.halfTime.away as away_goals_ht

from {{ source('world_cup', 'matches_external') }}