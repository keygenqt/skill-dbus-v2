project('server', 'cpp')

sdbus = dependency('sdbus-c++', version: '1.2.0')

executable('server', 
    [
        'src/main.cpp',
    ], 
    dependencies : [
        sdbus, 
    ]
)
