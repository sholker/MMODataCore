//  כמה קבוצות שחקנים ממדינות שונות עובדות יחד על משימות משותפות וכמה מהן מאותה מדינה


db.shared_quests.aggregate([
    { $unwind: "$player_ids" }, // פותח את המערך של 'player_ids', כך שכל ערך במערך הופך לדוקומנט נפרד, מה שמאפשר עיבוד נפרד של כל שחקן במשימה.

    {
        $lookup: {
            from: "player", // מציין את האוסף בו נבצע את החיפוש.
            localField: "player_ids", // השדה באוסף הנוכחי שישמש לצימוד.
            foreignField: "player_id", // השדה באוסף המטרה שלעומתו יתבצע הצימוד.
            as: "player_info" // השם של השדה שיכיל את התוצאות של החיפוש.
        }
    },

    { $unwind: "$player_info" }, // פותח את המערך שנוצר מה-$lookup כדי להמשיך ולעבד כל שחקן כדוקומנט נפרד.

    {
        $group: {
            _id: "$quest_id", // מקבץ את הנתונים לפי מזהה המשימה.
            countries: { $addToSet: "$player_info.country" } // מוסיף לקבוצה ייחודית של מדינות מהשחקנים במשימה זו.
        }
    },

    {
        $group: {
            _id: null, // קבוצה גלובלית לכל הדוקומנטים.
            total_shared_quest_combinations_different_county: { $sum: 1 }, // סופר את כל המשימות המשותפות ללא תלות במדינה.
            shared_quest_combinations_with_same_country: {
                $sum: {
                    $cond: [{ $eq: [{ $size: "$countries" }, 1] }, 1, 0] // בודק אם כל השחקנים מאותה משימה הם מאותה מדינה, ואם כן מחזיר 1, אחרת 0.
                }
            }
        }
    },

    {
        $project: {
            _id: 0, // מסתיר את שדה ה-_id מהתוצאה הסופית.
            total_shared_quest_combinations_different_county: 1, // מציג את מספר המשימות המשותפות עם שחקנים ממדינות שונות.
            shared_quest_combinations_with_same_country: 1 // מציג את מספר המשימות המשותפות עם שחקנים מאותה מדינה.
        }
    }
])



