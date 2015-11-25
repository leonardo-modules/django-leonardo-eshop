from django import template

from oscar.core.loading import get_model

from ..forms import AddToBasketForm, SimpleAddToBasketForm

Product = get_model('catalogue', 'product')

register = template.Library()

QNT_SINGLE, QNT_MULTIPLE = 'single', 'multiple'


@register.assignment_tag()
def basket_form(request, product, quantity_type='single'):
    if not isinstance(product, Product):
        return ''

    initial = {}
    if not product.is_parent:
        initial['product_id'] = product.id

    form_class = AddToBasketForm
    if quantity_type == QNT_SINGLE:
        form_class = SimpleAddToBasketForm

    form = form_class(request.basket, product=product, initial=initial)

    return form
