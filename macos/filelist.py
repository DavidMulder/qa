import os

basepath = '/Library/Frameworks/Mono.framework/Versions/Current'

files = [
    os.path.join(basepath,'bin','vbnc'),
    os.path.join(basepath,'lib','mono','2.0','Microsoft.VisualBasic.dll'),
    os.path.join(basepath,'share','man','man1','vbnc.1'),
    '/Library/Frameworks/Mono.framework/Commands/al',
    '/Library/Frameworks/Mono.framework/Commands/al1',
    '/Library/Frameworks/Mono.framework/Commands/al2',
    '/Library/Frameworks/Mono.framework/Commands/asp-state',
    '/Library/Frameworks/Mono.framework/Commands/asp-state1',
    '/Library/Frameworks/Mono.framework/Commands/asp-state2',
    '/Library/Frameworks/Mono.framework/Commands/caspol',
    '/Library/Frameworks/Mono.framework/Commands/cert2spc',
    '/Library/Frameworks/Mono.framework/Commands/certmgr',
    '/Library/Frameworks/Mono.framework/Commands/chktrust',
    '/Library/Frameworks/Mono.framework/Commands/csharp',
    '/Library/Frameworks/Mono.framework/Commands/dbsessmgr',
    '/Library/Frameworks/Mono.framework/Commands/dbsessmgr1',
    '/Library/Frameworks/Mono.framework/Commands/dbsessmgr2',
    '/Library/Frameworks/Mono.framework/Commands/disco',
    '/Library/Frameworks/Mono.framework/Commands/dtd2rng',
    '/Library/Frameworks/Mono.framework/Commands/dtd2xsd',
    '/Library/Frameworks/Mono.framework/Commands/fastcgi-mono-server',
    '/Library/Frameworks/Mono.framework/Commands/fastcgi-mono-server1',
    '/Library/Frameworks/Mono.framework/Commands/fastcgi-mono-server2',
    '/Library/Frameworks/Mono.framework/Commands/gacutil',
    '/Library/Frameworks/Mono.framework/Commands/gacutil1',
    '/Library/Frameworks/Mono.framework/Commands/gacutil2',
    '/Library/Frameworks/Mono.framework/Commands/genxs',
    '/Library/Frameworks/Mono.framework/Commands/genxs1',
    '/Library/Frameworks/Mono.framework/Commands/gmcs',
    '/Library/Frameworks/Mono.framework/Commands/httpcfg',
    '/Library/Frameworks/Mono.framework/Commands/ilasm',
    '/Library/Frameworks/Mono.framework/Commands/ilasm1',
    '/Library/Frameworks/Mono.framework/Commands/ilasm2',
    '/Library/Frameworks/Mono.framework/Commands/installvst',
    '/Library/Frameworks/Mono.framework/Commands/ipy',
    '/Library/Frameworks/Mono.framework/Commands/ipy2',
    '/Library/Frameworks/Mono.framework/Commands/ipyw',
    '/Library/Frameworks/Mono.framework/Commands/ipyw2',
    '/Library/Frameworks/Mono.framework/Commands/jay',
    '/Library/Frameworks/Mono.framework/Commands/macpack',
    '/Library/Frameworks/Mono.framework/Commands/makecert',
    '/Library/Frameworks/Mono.framework/Commands/mautil',
    '/Library/Frameworks/Mono.framework/Commands/mconfig',
    '/Library/Frameworks/Mono.framework/Commands/mcs',
    '/Library/Frameworks/Mono.framework/Commands/mcs1',
    '/Library/Frameworks/Mono.framework/Commands/mdassembler',
    '/Library/Frameworks/Mono.framework/Commands/mdoc',
    '/Library/Frameworks/Mono.framework/Commands/mdoc-assemble',
    '/Library/Frameworks/Mono.framework/Commands/mdoc-export-html',
    '/Library/Frameworks/Mono.framework/Commands/mdoc-export-msxdoc',
    '/Library/Frameworks/Mono.framework/Commands/mdoc-update',
    '/Library/Frameworks/Mono.framework/Commands/mdoc-validate',
    '/Library/Frameworks/Mono.framework/Commands/mdvalidater',
    '/Library/Frameworks/Mono.framework/Commands/mkbundle',
    '/Library/Frameworks/Mono.framework/Commands/mkbundle1',
    '/Library/Frameworks/Mono.framework/Commands/mkbundle2',
    '/Library/Frameworks/Mono.framework/Commands/mod',
    '/Library/Frameworks/Mono.framework/Commands/mod-mono-server',
    '/Library/Frameworks/Mono.framework/Commands/mod-mono-server1',
    '/Library/Frameworks/Mono.framework/Commands/mod-mono-server2',
    '/Library/Frameworks/Mono.framework/Commands/mono',
    '/Library/Frameworks/Mono.framework/Commands/mono-api-info',
    '/Library/Frameworks/Mono.framework/Commands/mono-cil-strip',
    '/Library/Frameworks/Mono.framework/Commands/mono-find-provides',
    '/Library/Frameworks/Mono.framework/Commands/mono-find-requires',
    '/Library/Frameworks/Mono.framework/Commands/mono-service',
    '/Library/Frameworks/Mono.framework/Commands/mono-service2',
    '/Library/Frameworks/Mono.framework/Commands/mono-shlib-cop',
    '/Library/Frameworks/Mono.framework/Commands/mono-test-install',
    '/Library/Frameworks/Mono.framework/Commands/mono-xmltool',
    '/Library/Frameworks/Mono.framework/Commands/monodis',
    '/Library/Frameworks/Mono.framework/Commands/monodocer',
    '/Library/Frameworks/Mono.framework/Commands/monodocs2html',
    '/Library/Frameworks/Mono.framework/Commands/monodocs2slashdoc',
    '/Library/Frameworks/Mono.framework/Commands/monograph',
    '/Library/Frameworks/Mono.framework/Commands/monolinker',
    '/Library/Frameworks/Mono.framework/Commands/monop',
    '/Library/Frameworks/Mono.framework/Commands/monop1',
    '/Library/Frameworks/Mono.framework/Commands/monop2',
    '/Library/Frameworks/Mono.framework/Commands/mozroots',
    '/Library/Frameworks/Mono.framework/Commands/nant',
    '/Library/Frameworks/Mono.framework/Commands/nunit-console',
    '/Library/Frameworks/Mono.framework/Commands/nunit-console2',
    '/Library/Frameworks/Mono.framework/Commands/pedump',
    '/Library/Frameworks/Mono.framework/Commands/permview',
    '/Library/Frameworks/Mono.framework/Commands/prj2make',
    '/Library/Frameworks/Mono.framework/Commands/resgen',
    '/Library/Frameworks/Mono.framework/Commands/resgen1',
    '/Library/Frameworks/Mono.framework/Commands/resgen2',
    '/Library/Frameworks/Mono.framework/Commands/secutil',
    '/Library/Frameworks/Mono.framework/Commands/setreg',
    '/Library/Frameworks/Mono.framework/Commands/sgen',
    '/Library/Frameworks/Mono.framework/Commands/signcode',
    '/Library/Frameworks/Mono.framework/Commands/smcs',
    '/Library/Frameworks/Mono.framework/Commands/sn',
    '/Library/Frameworks/Mono.framework/Commands/soapsuds',
    '/Library/Frameworks/Mono.framework/Commands/sqlsharp',
    '/Library/Frameworks/Mono.framework/Commands/vbnc',
    '/Library/Frameworks/Mono.framework/Commands/wsdl',
    '/Library/Frameworks/Mono.framework/Commands/wsdl1',
    '/Library/Frameworks/Mono.framework/Commands/wsdl2',
    '/Library/Frameworks/Mono.framework/Commands/xbuild',
    '/Library/Frameworks/Mono.framework/Commands/xsd',
    '/Library/Frameworks/Mono.framework/Commands/xsd2',
    '/Library/Frameworks/Mono.framework/Commands/xsp',
    '/Library/Frameworks/Mono.framework/Commands/xsp1',
    '/Library/Frameworks/Mono.framework/Commands/xsp2',

    
]

dirs = [
    '/Library/Frameworks/Mono.framework',
    '/Library/Frameworks/Mono.framework/Versions',
    os.path.join(basepath,'lib'),
    os.path.join(basepath,'bin'),
    os.path.join(basepath,'share'),
    os.path.join(basepath,'etc'),
    os.path.join(basepath,'include'),
    os.path.join(basepath,'Resources'),
    os.path.join(basepath,'lib','mono','gac','Microsoft.VisualBasic')
]

symlinks = [
    '/Library/Frameworks/Mono.framework/Commands',
    '/Library/Frameworks/Mono.framework/Headers',
    '/Library/Frameworks/Mono.framework/Home',
    '/Library/Frameworks/Mono.framework/Libraries',
    '/Library/Frameworks/Mono.framework/Mono',
    '/Library/Frameworks/Mono.framework/Versions/Current',
    '/usr/bin/al',
    '/usr/bin/al1',
    '/usr/bin/al2',
    '/usr/bin/asp-state',
    '/usr/bin/asp-state1',
    '/usr/bin/asp-state2',
    '/usr/bin/caspol',
    '/usr/bin/cert2spc',
    '/usr/bin/certmgr',
    '/usr/bin/chktrust',
    '/usr/bin/csharp',
    '/usr/bin/dbsessmgr',
    '/usr/bin/dbsessmgr1',
    '/usr/bin/dbsessmgr2',
    '/usr/bin/disco',
    '/usr/bin/dtd2rng',
    '/usr/bin/dtd2xsd',
    '/usr/bin/fastcgi-mono-server',
    '/usr/bin/fastcgi-mono-server1',
    '/usr/bin/fastcgi-mono-server2',
    '/usr/bin/gacutil',
    '/usr/bin/gacutil1',
    '/usr/bin/gacutil2',
    '/usr/bin/genxs',
    '/usr/bin/genxs1',
    '/usr/bin/gmcs',
    '/usr/bin/httpcfg',
    '/usr/bin/ilasm',
    '/usr/bin/ilasm1',
    '/usr/bin/ilasm2',
    '/usr/bin/installvst',
    '/usr/bin/ipy',
    '/usr/bin/ipy2',
    '/usr/bin/ipyw',
    '/usr/bin/ipyw2',
    '/usr/bin/jay',
    '/usr/bin/macpack',
    '/usr/bin/makecert',
    '/usr/bin/mautil',
    '/usr/bin/mconfig',
    '/usr/bin/mcs',
    '/usr/bin/mcs1',
    '/usr/bin/mdassembler',
    '/usr/bin/mdoc',
    '/usr/bin/mdoc-assemble',
    '/usr/bin/mdoc-export-html',
    '/usr/bin/mdoc-export-msxdoc',
    '/usr/bin/mdoc-update',
    '/usr/bin/mdoc-validate',
    '/usr/bin/mdvalidater',
    '/usr/bin/mkbundle',
    '/usr/bin/mkbundle1',
    '/usr/bin/mkbundle2',
    '/usr/bin/mod',
    '/usr/bin/mod-mono-server',
    '/usr/bin/mod-mono-server1',
    '/usr/bin/mod-mono-server2',
    '/usr/bin/mono',
    '/usr/bin/mono-api-info',
    '/usr/bin/mono-cil-strip',
    '/usr/bin/mono-find-provides',
    '/usr/bin/mono-find-requires',
    '/usr/bin/mono-service',
    '/usr/bin/mono-service2',
    '/usr/bin/mono-shlib-cop',
    '/usr/bin/mono-test-install',
    '/usr/bin/mono-xmltool',
    '/usr/bin/monodis',
    '/usr/bin/monodocer',
    '/usr/bin/monodocs2html',
    '/usr/bin/monodocs2slashdoc',
    '/usr/bin/monograph',
    '/usr/bin/monolinker',
    '/usr/bin/monop',
    '/usr/bin/monop1',
    '/usr/bin/monop2',
    '/usr/bin/mozroots',
    '/usr/bin/nant',
    '/usr/bin/nunit-console',
    '/usr/bin/nunit-console2',
    '/usr/bin/pedump',
    '/usr/bin/permview',
    '/usr/bin/prj2make',
    '/usr/bin/resgen',
    '/usr/bin/resgen1',
    '/usr/bin/resgen2',
    '/usr/bin/secutil',
    '/usr/bin/setreg',
    '/usr/bin/sgen',
    '/usr/bin/signcode',
    '/usr/bin/smcs',
    '/usr/bin/sn',
    '/usr/bin/soapsuds',
    '/usr/bin/sqlsharp',
    '/usr/bin/vbnc',
    '/usr/bin/wsdl',
    '/usr/bin/wsdl1',
    '/usr/bin/wsdl2',
    '/usr/bin/xbuild',
    '/usr/bin/xsd',
    '/usr/bin/xsd2',
    '/usr/bin/xsp',
    '/usr/bin/xsp1',
    '/usr/bin/xsp2',

]


# These files/dirs/links should NOT exist
baddirs = [
    os.path.join(basepath,'usr')
]
badfiles = [
    '/Library/Frameworks/Mono.framework/Commands/cilc',
    '/Library/Frameworks/Mono.framework/Commands/gapi2-codegen',
    '/Library/Frameworks/Mono.framework/Commands/gapi2-fixup',
    '/Library/Frameworks/Mono.framework/Commands/gapi2-parser',
    '/Library/Frameworks/Mono.framework/Commands/ikvm',
    '/Library/Frameworks/Mono.framework/Commands/ikvmc',
    '/Library/Frameworks/Mono.framework/Commands/ikvmstub',
    '/Library/Frameworks/Mono.framework/Commands/mjs',

]
badsymlinks = [
    '/usr/bin/cilc',
    '/usr/bin/gapi2-codegen',
    '/usr/bin/gapi2-fixup',
    '/usr/bin/gapi2-parser',
    '/usr/bin/ikvm',
    '/usr/bin/ikvmc',
    '/usr/bin/ikvmstub',
    '/usr/bin/mjs',

]


# vim:ts=4:expandtab:
