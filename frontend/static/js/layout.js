window.addEventListener('load', () => {

	const links = document.querySelectorAll('.nowhere');
	links.forEach(link => {
		
		link.addEventListener('click', (event) => {

			event.preventDefault();
			alert('This link redirect to nowhere');
		})
	})
})