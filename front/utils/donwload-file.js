const downloadFile = (url, filename) => {
    fetch(url)
        .then(response => response.blob())
        .then(blob => {
            const fileURL = window.URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.style.display = 'none';

            link.href = fileURL;

            link.setAttribute('download', `${filename}.csv`);

            link.click();

            window.URL.revokeObjectURL(fileURL);

            link.remove();
        });
};

export default downloadFile;

            
