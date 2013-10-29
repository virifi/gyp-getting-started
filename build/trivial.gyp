{
  'includes': ['common.gypi'],
  'make_global_settings': [
    ['CXX','/usr/bin/clang++'],
    ['LINK','/usr/bin/clang++'],
  ],
  'target_defaults': {
    'conditions': [
      ['OS == "win"', {
        'msvs_settings':{
          'VCCLCompilerTool': {
            'WarningLevel': '4', # /W4
          },
        }
      }], # OS == "win"
      ['OS == "mac"', {
        'xcode_settings': {
          'GCC_VERSION': 'com.apple.compilers.llvm.clang.1_0',
          'CLANG_CXX_LANGUAGE_STANDARD': 'c++0x',
		  'MACOSX_DEPLOYMENT_TARGET': '10.8', # OS X Deployment Target: 10.8
        },
      }], # OS == "mac"
    ],
  },
  'targets': [
    {
      'target_name': 'trivial_engine',
      'product_name': 'TrivialEngine',
      'type': 'static_library',
      'include_dirs': [
        '../include',
      ],
      'sources': [
        '../src/Entity.cpp',
      ],
      'conditions': [
        ['OS == "mac"', {
          'xcode_settings': {
            'OTHER_CPLUSPLUSFLAGS': ['-std=c++11','-stdlib=libc++'],
          },
        }], # OS == "mac"
      ],
    },
    {
      'target_name': 'trivial_test',
      'product_name': 'TrivialTest',
      'type': 'executable',
      'dependencies': [
        'trivial_engine',
      ],
      'include_dirs': [
        '../include',
      ],
      'sources': [
        '../test/EntityTest.cpp',
      ],
      'conditions': [
        ['OS == "mac"', {
          'xcode_settings': {
            'OTHER_CPLUSPLUSFLAGS': ['-std=c++11','-stdlib=libc++'],
            'OTHER_LDFLAGS': ['-stdlib=libc++'],
          },
        }], # OS == "mac"
      ],
    },
  ]
}
