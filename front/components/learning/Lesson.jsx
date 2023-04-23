import React, { useEffect, useState } from 'react';

import { createLessonLike, deleteLessonLike } from '../../services/learning';
import CustomButton from './CustomButton';
import WordReinforcement from './WordReinforcement';



function Lesson({ lesson, activity, nextLessonHandler }) {
    const [fav, setFav] = useState(null);
    const [showWordReinforcement, setShowWordReinforcement] = useState(false);
    const [showButton, setShowButton] = useState(true);

    useEffect(() => {
        if (lesson.is_liked) {
            setFav(lesson.is_liked);
        } else {
            setFav(null);
        }
    }, [lesson]);

    const favHandler = () => {
        if (!fav) {
            createLessonLike({
                lesson: lesson.id
            }).then((response) => {
                setFav(response);
            });
        } else {
            deleteLessonLike(fav.id).then((response) => {
                setFav(null);
            });
        }
    }

    const formatContent = (content) => {

        if (!content) {
            return '';
        }

        // list format
        content = content.replace(/<ul>/g, '<ul class="list-disc ml-4">');

        return content
    }

    const getHeartIcon = () => {
        return fav ? '/static/icons/heart.png' : '/static/icons/heart-empty.png';
    }


    const handleButton = () => {

        if (lesson.lesson_type === 'Conversation') {
            setShowWordReinforcement(true);
            setShowButton(false);
            return;
        }

        setShowButton(true);
        nextLessonHandler();

        return;
    }

    const handleWordReinforcement = () => {

        setShowWordReinforcement(false);
        setShowButton(true);

        nextLessonHandler();
        return;
    }


    return (
        <div className="flex flex-col mb-2">
            <div className="rounded shadow-lg p-3 border border-gray-300">
                <div className="flex justify-between">
                    <div className='flex flex-col' >
                        <h2 className="text-xl font-bold text-gray-700">
                            {lesson.title}
                        </h2>
                        <span className="text-sm text-gray-600">
                            {lesson.lesson_type} - Level: {lesson.level}
                        </span>
                    </div>
                    <button className="bg-white rounded-full p-2 flex-shrink-0
                    " onClick={favHandler}>
                        <img alt="heart" className="w-6 h-6" src={getHeartIcon()} />
                    </button>

                </div>
                <div className="mt-2 mb-5 text-gray-600" dangerouslySetInnerHTML={{ __html: formatContent(lesson.content) }}></div>
                {
                    (showButton) && (
                        <div className="flex justify-end w-100">
                            <CustomButton onClick={handleButton} wFade={showWordReinforcement} >
                                Continuar <span aria-hidden="true">&rarr;</span>
                            </CustomButton>
                        </div>
                    )
                }
            </div>

            {
                showWordReinforcement && (
                    <WordReinforcement activity={activity} onClick={handleWordReinforcement} isOpen={showWordReinforcement} />
                )
            }
        </div>
    );
}

export default Lesson;