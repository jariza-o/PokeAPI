/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   login.js                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jariza-o <jariza-o@student.42malaga.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/10/21 15:59:37 by jariza-o          #+#    #+#             */
/*   Updated: 2024/10/21 15:59:42 by jariza-o         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

async function login() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    const response = await fetch('https://your-backend-api.com/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password })
    });

    if (response.ok) {
        const data = await response.json();
        // Procesa la respuesta del backend
        alert('Login successful!');
        // Redirige o realiza otras acciones según sea necesario
    } else {
        // Maneja el error
        alert('Login failed. Please check your credentials.');
    }
}