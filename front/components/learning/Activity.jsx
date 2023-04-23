import React, { useState, useEffect } from 'react';
import { createUserActivityLike, deleteUserActivityLike, getUserActivity } from '../../services/learning';

function Activity({ activity_id, children, data = null, classNames = "", wFav = true }) {

    const [activity, setActivity] = useState({});
    const [fav, setFav] = useState(null);


    const favHandler = () => {
        if (!fav) {
            createUserActivityLike({
                activity: activity.id
            }).then((response) => {
                setFav(response);
            });
        } else {
            deleteUserActivityLike(fav.id).then((response) => {
                setFav(null);
            });
        }
    }

    const getHeartIcon = () => {
        return fav ? '/static/icons/heart.png' : '/static/icons/heart-empty.png';
    }


    useEffect(() => {
        if (data) {
            setActivity(data);

            if (data.is_liked) {
                setFav(data.is_liked);
            }


            return;
        }

        getUserActivity(activity_id).then((activity) => {
            setActivity(activity);

            if (activity.is_liked) {
                setFav(activity.is_liked);
            }
        });

    }, []);

    return (
        <div className={classNames != "" ? classNames : 'rounded shadow-lg p-3 border border-gray-300'}>
            <div className="flex justify-between">
                <h2 className="text-xl font-bold text-gray-700">
                    {activity.title}
                </h2>
                {
                    wFav && (
                        <button className="bg-white rounded-full p-2" onClick={favHandler}>
                            <img alt="heart" className="w-6 h-6" src={getHeartIcon()} />
                        </button>
                    )
                }
            </div>
            <div className="mb-2">
                <ul>
                    {
                        activity.lessons && activity.lessons.map((lesson, index) => {
                            return (
                                <li key={index} className="flex justify-between items-center text-gray-700 py-2 border-b border-gray-300">
                                    <div className="flex flex-col">
                                        <span className="text-sm font-bold">
                                            {lesson.title}
                                        </span>
                                        <span className="text-xs text-gray-500">
                                            Level: {lesson.level}
                                        </span>
                                    </div>

                                    <span className="text-xs text-gray-500">
                                        {lesson.lesson_type}

                                    </span>
                                </li>
                            );
                        })
                    }

                </ul>

                {
                    children
                }
            </div>
        </div>
    );
}

export default Activity;