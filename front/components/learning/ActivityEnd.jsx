import React from 'react';

function ActivityEnd() {
    return (
        <div className="flex flex-col items-center justify-center text-center w-full h-full">
            <p className="text-2xl font-bold text-gray-700">
                <span className="text-orange-500" >¡Felicidades!</span> Has completado tu actividad diaria.
            </p>
            <p className="text-gray-700 mt-2">
                Si quieres seguir aprendiendo, puedes encontrar otras lecciones en
            </p>
            <a href="/feed/" className="bg-orange-500 text-white p-2 rounded text-center block mt-5">
                Actividades <span aria-hidden="true">&rarr;</span>
            </a>
        </div>
    );
}

export default ActivityEnd;