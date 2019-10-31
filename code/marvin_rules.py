default = {
    'life' : {
        'Action': None,
        'CatalogSentence': 'Life'
    }
}

default.update({
    'I have a problem' : {
        'Action': None,
        'CatalogSentence': 'IHaveAProblem'
    }
})

default.update({
    'Wake': {
    'Action': 'wakeup',
    'CatalogSentence': 'WakeUp'
    }
})

default.update({
    'open': {
    'Action': 'openAplication',
    'CatalogSentence': 'RandomExecution'
    }
})

default.update({
    'Error': {
    'Action': 'openAplication',
    'CatalogSentence': 'ErrorExecution'
    }
})

default.update({
    'Default': {
    'Action': None,
    'CatalogSentence': 'RandomClaim'
    }
})
