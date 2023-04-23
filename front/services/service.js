const baseUrl = '/api';

function getCSRFToken() {
    const name = 'csrftoken';
    const cookieValue = document.cookie
        .split('; ')
        .find(row => row.startsWith(name))
        .split('=')[1];
    return cookieValue;
}

export const get = async (url) => {
    const response = await fetch(baseUrl + url);
    return response.json();
}

export const post = async (url, data) => {
    const response = await fetch(baseUrl + url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken(),
        },
        body: JSON.stringify(data)
    });
    return response.json();
}

export const destroy = async (url) => {
    const response = await fetch(baseUrl + url, {
        method: 'DELETE',
        headers: {
            'X-CSRFToken': getCSRFToken(),
        },
    });
    return response.status === 204;
}