%define device sparkler

%define kernel_pkg kernel-adaptation-msm8909

%define kernel /boot/zImage
%define dtb /boot/qcom-msm8909-nokia-sparkler.dtb
%define cmdline "earlycon console=ttyMSM0,115200 console=tty1"

%define mkbootimg_cmd cat %{kernel} %{dtb} > kernel-dtb && mkbootimg --kernel kernel-dtb --ramdisk %{initrd} --cmdline %{cmdline} --output

%define root_part_label userdata
%define factory_part_label system

%define display_brightness_path /sys/class/backlight/backlight/brightness
%define display_brightness 1

%define lvm_root_size 2400

%define initrd_use_lz4 1

BuildRequires:  mipi-dbi-configs

%include device-img-boot-mainline/device-img-boot.inc
