import React, { useEffect, useState } from 'react';
import ReportList from './ReportList';

import Swal from 'sweetalert2'
import { createReport, getReport, getReports } from '../../services/analitycs';
import Toast from './Toast';
import downloadFile from '../../utils/donwload-file';



function Reports() {

    const [data, setData] = useState(null);
    const [newReport, setNewReport] = useState(null);
    const [openToast, setOpenToast] = useState(false);
    const [toast, setToast] = useState(null);



    useEffect(() => {
        getReports().then((response) => {
            setData(response);
        });
    }, []);

    useEffect(() => {
        if (newReport) {
            setTimeout(() => {
                // call peridically to get file status
                getReport(newReport.slug).then((response) => {
                    console.log(response);
                    if (response.file) {

                        setOpenToast(true);
                        setToast('Reporte generado');

                        setNewReport(null);

                        // download file
                        window.open(response.file, '_blank');
                        downloadFile(response.file, response.name)

                    }
                });
            }, 5000);
        }
    }, [newReport]);

    const onCloseToast = () => {
        setOpenToast(false);
    }

    const handleNewReport = () => {

        Swal.fire({
            title: 'Nuevo reporte',
            input: 'select',
            inputOptions: {
                'activity': 'Actividad',
                'user': 'Usuario',
                'lesson': 'Lección',
            },
            inputPlaceholder: 'Selecciona un tipo de reporte',
            showCancelButton: true,
            confirmButtonText: 'Continuar',
            cancelButtonText: 'Cancelar',
            showLoaderOnConfirm: true,
            preConfirm: (type) => {
                //
            },
            allowOutsideClick: () => !Swal.isLoading()
        }).then((result) => {
            if (result.isConfirmed) {
                createReport({
                    report_type: result.value,
                }).then((response) => {
                    console.log(response);

                    if (!response.id) {
                        Swal.fire({
                            title: 'Error',
                            text: 'No se pudo crear el reporte',
                            icon: 'error',
                            confirmButtonText: 'Continuar',
                        });
                        return;
                    }

                    setOpenToast(true);
                    setToast('Creando reporte, por favor espere...');            

                    setNewReport(response);
                    setData([...data, response]);

                });
            }
        });               

    }

    return (
        <div className="flex flex-col w-full">
            <div className="flex justify-between items-center mb-3 py-2">
                <h3 className="text-gray-700 text-lg font-bold">
                    Reportes
                </h3>
                <button className="bg-blue-500 text-white rounded shadow-sm p-2" onClick={handleNewReport}>
                    Nuevo reporte
                </button>
            </div>

            <ReportList data={data} />

            {
                openToast && <Toast msg={toast} isOpen={openToast} onClose={onCloseToast} />
            }
        </div>
    );
}

export default Reports;