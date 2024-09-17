db.player.aggregate([
    {
        $group: { // מאגד documents לפי quest_id
            _id: "$country",  // קיבוץ לפי שדה ה-country - כל קבוצה היא מדינה.
            highest_level_player: { $first: "$$ROOT" },// שמירה על המסמך הראשון בכל קבוצה - זה יהיה המסמך המייצג של המדינה.
            max_level: { $max: "$level" }  // חישוב הערך המקסימלי של רמת השחקן באותה מדינה.
        }
    },
    {
        $project: {
            _id: 0,  // לא להציג את שדה ה-_id בתוצאה.
            country: "$_id",  // הצגת שדה ה-country שהתבסס על ה-_id מקבוצת ה-$group.
            username: "$highest_level_player.username",  // הצגת שם המשתמש של השחקן עם הרמה הגבוהה ביותר.
            level: "$max_level"  // הצגת הרמה המקסימלית כפי שנחוש ב-$group.
        }
    }
])

