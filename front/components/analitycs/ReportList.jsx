import React from 'react';

function ReportList({ data }) {





    return (
        <div className="flex flex-col mt-5">

            <div className="flex justify-between mb-3">
                <div className="flex self-end">
                    <input type="text" placeholder='Search' className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"/>
                    <button className="bg-gray-200 rounded shadow-sm p-2 ml-2" onClick={()=>'Hello'}>
                        <img src="/static/icons/search.png" alt="" className='w-5 h-5' />
                    </button>
                </div>
                <div className="flex">
                    <div className="mr-4">
                        <label className="block text-gray-700 text-sm font-bold mb-2">
                            Tipo de reporte
                        </label>

                        <select name="" id="" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                            <option value="">Todos</option>
                            <option value="">Activity</option>
                            <option value="">Users</option>
                            <option value="">Lesson</option>
                        </select>
                    </div>
                    <div className="">
                        <label className="block text-gray-700 text-sm font-bold mb-2">
                            Ordenar por
                        </label>

                        <select name="" id="" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
                            <option value="">Fecha de creación (desc)</option>
                            <option value="">Fecha de creación (asc)</option>
                            <option value="">Nombre</option>
                            <option value="">Tipo</option>
                        </select>
                    </div>
                </div>
            </div>


            <table className="table-auto mt-5">
                <thead>
                    <tr>
                        <th>Nombre</th>
                        <th>Tipo</th>
                        <th>Fecha de creación</th>
                        <th>Descargar</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        data && data.map((item, index) => (
                            <tr key={index} >
                                <td><b>{item.name}</b></td>
                                <td>{item.report_type}</td>
                                <td>{item.created_at}</td>
                                <td>
                                    <div className="flex justify-center">
                                        <button className="flex bg-blue-500 rounded shadow-sm p-2" onClick={()=>'Hello'}>
                                            <span className='text-white text-center'>Descargar</span> <img src="/static/icons/download.png" alt="" className='w-5 h-5' />
                                        </button>
                                    </div>
                                </td>
                            </tr>
                        ))
                    }
                </tbody>
            </table>
        </div>
    );
}

export default ReportList;