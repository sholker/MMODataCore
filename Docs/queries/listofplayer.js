// כל השחקנים הנמצאים ברמה 3 ומעלה


db.player.find(
    { level: { $gte: 3 } }, // all players with level 3 and above (select * from player where level >= 3 geater)
    { _id: 0, player_id: 1, username: 1, level: 1 } // display
)


