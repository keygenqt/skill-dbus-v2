project('client', 'cpp')

sdbus = dependency('sdbus-c++', version: '1.2.0')

executable('client', 
    [
        'src/main.cpp',
    ], 
    dependencies : [
        sdbus, 
    ]
)
