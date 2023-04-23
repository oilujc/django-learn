import React, { useEffect, useState } from 'react';
import { createUserActivity } from '../../services/learning';
import { getTimeline } from '../../services/timeline';
import Activity from '../learning/Activity';
import CustomButton from '../learning/CustomButton';

function Timeline() {

    const [timelines, setTimelines] = useState([]);

    useEffect(() => {

        getTimeline().then((response) => {
            setTimelines(response);
        });

    }, []);

    const formatDate = (date) => {
        // MM DD, YYYY
        
        const d = new Date(date);
        const month = d.toLocaleString('default', { month: 'long' });
        const day = d.getDate();
        const year = d.getFullYear();

        return `${month} ${day}, ${year}`;

    }

    const handleActivityButton = (item) => {

        console.log(item);

        createUserActivity({
            ref: item.slug
        }).then((response) => {
            window.location.href = `/learning/learn/?a=${response.slug}`;
        });
    }


    return (
        <div className="flex flex-col pb-20">
            <div className="flex justify-between items-center mb-3 py-2">
                <h3 className="text-gray-700 text-lg font-bold">
                    Timeline
                </h3>
            </div>

            <ol className="relative border-l border-gray-200 dark:border-gray-700">
                {
                    timelines.map((timeline, index) => {
                        return (
                            <li key={index} className="mb-10 ml-4">
                                <div
                                    className="absolute w-3 h-3 bg-gray-200 rounded-full mt-1.5 -left-1.5 border border-white dark:border-gray-900 dark:bg-gray-700">
                                </div>
                                <time className="mb-1 text-sm font-normal leading-none text-gray-400 dark:text-gray-500">
                                    { formatDate(timeline.created_at) }
                                </time>
                                {
                                    timeline.action === 'daily_activity_completed' || timeline.action === 'custom_activity_completed' ? (
                                        <Activity activity_id={timeline.item.id} data={timeline.item} >
                                            {
                                                timeline.action === 'daily_activity_completed' && timeline.item.child.length === 0 ? (
                                                    <div className="flex justify-end w-100 mt-2">
                                                        <CustomButton onClick={handleActivityButton} args={timeline.item} backgroundColor='bg-orange-500' textColor='text-white' >
                                                            Volver a practicar <span aria-hidden="true">&rarr;</span>
                                                        </CustomButton>
                                                    </div>
                                                ) : null
                                            }
                                        </Activity>
                                    ) : null
                                        
                                }
                            </li>
                        );
                    })
                }
            </ol>

        </div>
    );
}

export default Timeline;