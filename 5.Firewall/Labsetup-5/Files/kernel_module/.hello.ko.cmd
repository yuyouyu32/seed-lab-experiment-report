cmd_/home/seed/Share/Labsetup-5/Files/kernel_module/hello.ko := ld -r -m elf_x86_64  -z max-page-size=0x200000  --build-id  -T ./scripts/module-common.lds -o /home/seed/Share/Labsetup-5/Files/kernel_module/hello.ko /home/seed/Share/Labsetup-5/Files/kernel_module/hello.o /home/seed/Share/Labsetup-5/Files/kernel_module/hello.mod.o;  true
