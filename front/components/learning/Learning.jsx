import React, { useState, useEffect } from 'react';
import { getLesson, createActivityProgress, getUserActivity } from '../../services/learning';
import ActivityEnd from './ActivityEnd';
import Lesson from './Lesson';
import ActivityRating from './ActivityRating';
import ActivityHelp from './ActivityHelp';


function Learning({ current_lesson, user_activity_id }) {

    const [lesson, setLesson] = useState({});
    const [activity, setActivity] = useState(null);
    const [is_completed, setIsCompleted] = useState(false);
    const [isHelpOpen, setIsHelpOpen] = useState(false);

    const nextLessonHandler = () => {
        createActivityProgress({
            lesson: lesson.id,
            ref: activity.slug
        }).then((response) => {

            activity.progress_count = activity.progress_count + 1;

            if (activity.lesson_count === activity.progress_count && !activity.next_lesson) {
                setIsCompleted(true);
                return;
            }

            if (response.next_lesson) {
                setLesson(response.next_lesson);
            }

            window.scrollTo({ top: 0, behavior: 'smooth' })
            return;
        });
    }

    useEffect(() => {
        getUserActivity(user_activity_id).then((activity) => {
            setActivity(activity);

            if (activity.lesson_count === activity.progress_count) {
                setIsCompleted(true);
                return;
            }

            getLesson(current_lesson).then((lesson) => {
                setLesson(lesson);
            });

        });
    }, []);

    const openHelpHandler = () => {
        setIsHelpOpen(!isHelpOpen);
    }

    return (
        <div className="flex flex-col">
            <div className="flex justify-between items-center mb-3 py-2">
                <h3 className="text-gray-700 text-lg font-bold">
                    {activity && activity.title}
                </h3>
                <button className="bg-white rounded-full p-2" onClick={openHelpHandler}>
                    <img src="/static/icons/help.png" alt="" className="w-6 h-6" />
                </button>
            </div>
            <div className='flex flex-col'>
                {
                    (is_completed && !activity.is_rating) && <ActivityRating activity={activity} />
                }

                {
                    (is_completed && activity.is_rating) && <ActivityEnd />
                }

                {
                    (!is_completed) && <Lesson lesson={lesson} activity={activity} nextLessonHandler={nextLessonHandler} />
                }
            </div>
            
            {
                isHelpOpen && <ActivityHelp onToggle={openHelpHandler} isOpen={isHelpOpen}  />
            }
        </div>

    );
}

export default Learning;