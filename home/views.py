from django.shortcuts import render

def home(request):
    
    grid_elements = [
        {
            'a_href'    : 'financial_planning:financial_planning',
            'div_class' : 'grid-element-container first-element',
            'i_id'      : 'icon-money', 
            'i_class'   : 'fa fa-money',
            'p_id'      : 'title-controle-financeiro'
        },
        {
            'a_href'    : 'financial_planning:financial_planning',
            'div_class' : 'grid-element-container second-element',
            'i_id'      : '', 
            'i_class'   : '',
            'p_id'      : ''
        },
        {
            'a_href'    : 'financial_planning:financial_planning',
            'div_class' : 'grid-element-container third-element',
            'i_id'      : '', 
            'i_class'   : '',
            'p_id'      : ''
        },
    ]
   
    return render(request, 'home/index.html', {'grid_elements': grid_elements})

