import React, { useEffect, useState } from "react";

function ActivityHelp({ isOpen, onToggle }) {

    const [animationClass, setAnimationClass] = useState('opacity-0');

    useEffect(() => {
        if (isOpen) {
            setTimeout(() => {
                setAnimationClass('flip-vertical-left');
            }, 100);
        } else {
            setAnimationClass('');
        }
    }, [isOpen]);

    const closeHandler = (e) => {
        e.preventDefault();

        setAnimationClass('flip-vertical-right');

        setTimeout(() => {
            onToggle();
        }, 400);
    }

    return (
        <div className={`fixed top-20 left-0 w-full h-[calc(100vh-4rem)] z-50 flex flex-col bg-white px-6 pb-20` + animationClass}>
            <div className="rounded h-full shadow-lg p-3 border border-gray-300">
                <div className="flex justify-between mb-2">
                    <h2 className="text-xl font-bold text-gray-700">
                        Ayuda
                    </h2>
                    <button className="bg-white rounded-full p-2" onClick={closeHandler}>
                        <img alt="heart" className="w-5 h-5" src="/static/icons/close.png" />
                    </button>
                </div>

                <div className="mb-2 text-gray-700">
                    <p>
                        Te presentamos una serie de actividades que te ayudarán a mejorar tu nivel de inglés.
                    </p>

                    <p>
                        Cada actividad está compuesta por una serie de lecciones que te ayudarán a mejorar tu nivel de inglés.
                    </p>

                    <p>
                        Al final de cada lección encontrarás un ejercicio que te ayudará a practicar lo aprendido.
                    </p>

                    <p className="mt-2">
                        Las lecciones estan organizadas en 4 tipos:
                    </p>

                    <ul className="mt-2" >
                        <li>
                            <span className="font-bold">Conversation:</span> En esta lección encontrarás una conversación en inglés en la que deberás leer cuidadosamente y luego indicar cuales son las palabras que no entiendes.
                        </li>    
                        <li>
                            <span className="font-bold">Grammar:</span> En esta lección encontrarás una explicación de una regla gramatical en inglés.
                        </li>
                        <li>
                            <span className="font-bold">Word Reinforcement:</span> En esta lección podrás encontrar las palabras que no entiendes, ver su traducción y ejemplos de uso.
                        </li>
                        <li>
                            <span className="font-bold">Quiz:</span> En esta lección encontrarás un ejercicio de preguntas en base a lo aprendido en las lecciones anteriores.
                        </li>
                    </ul>                   
                </div>
            </div>
        </div>
    );
}

export default ActivityHelp;