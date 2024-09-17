// player
db.player.createIndex({ player_id: 1 }); // Index on player_id (ascending)
db.player.createIndex({ level: 1 }); // Index on level (ascending)

// quest
db.quest.createIndex({ quest_id: 1 })  // Index on quest_id (ascending)

// player_action
db.player_action.createIndex({ player_id: 1, action_type: 1 }); // Compound index on player_id and action_type
db.player_action.createIndex({ quest_id: 1 }); // Index on quest_id (ascending)

//shared_quest
db.shared_quests.createIndex({ "player_ids": 1 }); // Index on player_ids (ascending)


/*
player.player_id
השפעה: האינדקס מאפשר ל-MongoDB למצוא את השחקן המבוקש באופן מהיר
 מאוד על ידי חיפוש ישיר באינדקס במקום לסרוק את כל האוסף. זהו שימוש
יעיל במיוחד כאשר האפליקציה דורשת גישה תכופה לנתוני שחקנים ספציפיים.
 */

/*
player.level
השפעה: האינדקס מאפשר חיפוש וסינון יעילים של שחקנים לפי רמתם.
 שאילתות שמחפשות שחקנים על פי רמה ייהנו מביצועים משופרים מכיוון
שהמנוע יכול לעבור על האינדקס במקום על כל הנתונים.
 */
/*
plyer_action. player_id, action_type
השפעה: האינדקס המורכב מאפשר למצוא במהירות פעולות ספציפיות
 שבוצעו על ידי שחקן מסוים.
 האינדקס מאפשר גישה ישירה לפעולות הרלוונטיות ללא צורך לסרוק את כל האוסף,
מה שמייעל באופן משמעותי את זמני החיפוש והעיבוד.
 */
/*
player_action.quest_id
השפעה: אינדקס זה מאפשר גישה מהירה לכל המשימות המשותפות שבהן מעורב שחקן ספציפי.
 זה יכול להיות שימושי במיוחד
כאשר נדרש לעקוב אחר מעורבות של שחקנים במשימות מרובות,
 כמו בשאילתות ניתוח או דיווח.
 */
/* shared_quests

 */



