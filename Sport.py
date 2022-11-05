class Sport:
    key = None
    group = None
    title = None
    description = None
    active = None
    hasOutrights = None


    def __init__(self, sportJSON):
        self.key = sportJSON['key']
        self.group = sportJSON['group']
        self.title = sportJSON['title']
        self.description = sportJSON['description']
        self.active = sportJSON['active']
        self.hasOutrights = sportJSON['has_outrights']
