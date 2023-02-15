from django import forms

class FiltroTecidosReferenciaForm(forms.Form):
    referencia = forms.CharField(required=False)

class FiltroTecidosTipoForm(forms.Form):    
    tipo = forms.ChoiceField(choices=[('linho', 'Linho'), ('camurça', 'Camurça'), ('mescla', 'Mescla'), ('moletom', 'Moletom')],
                               required=False, widget=forms.Select(attrs={'class': 'form-control'}))
  
class FiltroTecidosCorForm(forms.Form):    
    cor = forms.ChoiceField(choices=[('branco','Branco'), ('preto', 'Preto'), ('cinza', 'Cinza'), ('chumbo', 'Chumbo'), ('vermelho','Vermelho'), ('vinho', 'Vinho'), ('coral', 'Coral'), ('laranja', 'Laranja'), ('amarelo', 'Amarelo'), ('amarelo canário', 'Amarelo Canário'), ('amarelo neon', 'Amarelo Neon'), ('marrom', 'Marrom'), ('caramelo', 'Caramelo'), ('caqui', 'Caqui'), ('bege','Bege'), ('rosa bebê', 'Rosa Bebê'), ('rosa neon', 'Rosa Neon'), ('pink', 'Pink'), ('azul claro', 'Azul Claro'), ('azul turquesa', 'Azul Turquesa'), ('azul royal', 'Azul Royal'), ('azul marinho', 'Azul Marinho'), ('roxo', 'Roxo'), ('verde lodo', 'Verde Lodo'), ('verde sinuca', 'Verde Sinuca'), ('verde bandeira', 'Verde Bandeira'), ('verde limão', 'Verde Limão'), ('verde água', 'Verde Água')],
                             required=False, widget=forms.Select(attrs={'class': 'form-control'}))