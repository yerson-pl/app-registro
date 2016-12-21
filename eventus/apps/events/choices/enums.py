from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst


M = 'M'
F = 'F'
GENERO_CHOICES = (
    (M, _('Masculino')),
    (F, capfirst(_('Femenino'))),
)

AZANGARO = 'Azángaro'
CARABAYA = 'Carabaya'
CHUCUITO = 'Chucuito'
ELCOLLAO = 'El Collao'
HUANCANE = 'Huancané'
LAMPA = 'Lampa'
MELGAR = 'Melgar'
MOHO = 'Moho'
PUNO = 'Puno'
SANANTONIO_DE_PUTINA = 'San Antonio de Putina'
SAN_ROMAN = 'San Román'
SANDIA = 'Sandia'
YUNGUYO = 'Yunguyo'

PROVINCIAS_CHOICES = (
    (AZANGARO, _('Azángaro')),
    (CARABAYA, _('Carabaya')),
    (CHUCUITO, _('Chucuito')),
    (ELCOLLAO, _('El Collao')),
    (HUANCANE, _('Huancané')),
    (LAMPA, _('Lampa')),
    (MELGAR, _('Melgar')),
    (MOHO, _('Moho')),
    (PUNO, _('Puno')),
    (SANANTONIO_DE_PUTINA, _('San Antonio de Putina')),
    (SAN_ROMAN, _('San Román')),
    (SANDIA, _('Sandia')),
    (YUNGUYO, capfirst(_('Yunguyo'))),
)


FACEBOOK = 'Facebook'
TWITER = 'Twiter'
Amigo = 'Amigo'
PUBLICIDAD_CALLE = 'publicidad calle'
OTROS = 'Otros'

ENTERECE_CHOICES = (
    (FACEBOOK, 'Facebook'),
    (TWITER, 'Twiter'),
    (Amigo, 'Amigo'),
    (PUBLICIDAD_CALLE, 'publicidad calle'),
    (OTROS, 'Otros')
)
