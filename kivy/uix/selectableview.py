from kivy.properties import NumericProperty, BooleanProperty


class SelectableView(object):
    '''The :class:`SelectableView` mixin is used with list items and other
    classes that are to be instantiated in a list view or other classes
    which use a selection-enabled adapter such as ListAdapter. select() and
    deselect() can to be overridden with display code to mark items as
    selected or not, if desired.
    '''

    index = NumericProperty(-1)
    '''The index into the underlying data list or the data item this view
    represents.
    '''

    is_selected = BooleanProperty(False)
    '''A SelectableView instance carries this property, which should be kept
    in sync with the equivalent property the data item represents.
    '''

    def __init__(self, **kwargs):
        super(SelectableView, self).__init__(**kwargs)

    def select(self, *args):
        '''The list item is responsible for updating the display for
        being selected, if desired.
        '''
        self.is_selected = True

    def deselect(self, *args):
        '''The list item is responsible for updating the display for
        being unselected, if desired.
        '''
        self.is_selected = False
