let selectedColor = null;

            document.querySelectorAll('.color-box').forEach(colorBox => {
                colorBox.addEventListener('click', function () {
                    selectedColor = this.style.backgroundColor; // Pega a cor do estilo
                    document.querySelectorAll('.color-box').forEach(box => {
                        box.style.border = '2px solid #555';
                    });
                    this.style.border = '4px solid black';
                });
            });

            document.querySelectorAll('td').forEach(cell => {
                cell.addEventListener('click', function () {
                    if (selectedColor) {
                        this.style.backgroundColor = selectedColor; // Aplica a cor selecionada
                    } else {
                        alert('Selecione uma cor primeiro!');
                    }
                });
            });

            document.querySelectorAll('.answer-list li').forEach(item => {
                item.addEventListener('click', function () {
                    this.classList.toggle('selected');
                });
            });