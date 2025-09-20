document.addEventListener('DOMContentLoaded', function() {
    const inputPreco = document.getElementById('price');
    
    // Formatar valor inicial se existir
    if (inputPreco.value) {
        inputPreco.value = formatarPreco(inputPreco.value);
    }
    
    // Evento de input para validação em tempo real
    inputPreco.addEventListener('input', function(e) {
        let valor = e.target.value;
        
        // Remover caracteres inválidos
        valor = valor.replace(/[^\d,.;]/g, '');
        
        // Substituir ponto por vírgula
        valor = valor.replace(/\./g, ',');
        
        // Permitir apenas uma vírgula (separador decimal)
        const partes = valor.split(',');
        if (partes.length > 2) {
            valor = partes[0] + ',' + partes.slice(1).join('');
        }
        
        // Limitar casas decimais a 2
        if (partes.length === 2 && partes[1].length > 2) {
            valor = partes[0] + ',' + partes[1].substring(0, 2);
        }
        
        e.target.value = valor;
    });
    
    // Evento de blur para formatação final
    inputPreco.addEventListener('blur', function(e) {
        e.target.value = formatarPreco(e.target.value);
    });
    
    // Evento de focus para remover formatação temporária
    inputPreco.addEventListener('focus', function(e) {
        e.target.value = e.target.value.replace(/[^\d,]/g, '');
    });
    
    // Função para formatar o preço
    function formatarPreco(valor) {
        if (!valor) return '';
        
        // Remover tudo exceto números e vírgula
        valor = valor.toString().replace(/[^\d,]/g, '');
        
        // Se não tiver vírgula, adicionar ,00
        if (!valor.includes(',')) {
            valor += ',00';
        }
        
        // Garantir duas casas decimais
        const partes = valor.split(',');
        if (partes.length === 2) {
            partes[1] = partes[1].padEnd(2, '0').substring(0, 2);
            valor = partes.join(',');
        }
        
        return valor;
    }
    
    // Função para obter o valor numérico (opcional)
    function obterValorNumerico(valorFormatado) {
        return parseFloat(valorFormatado.replace(',', '.'));
    }
});