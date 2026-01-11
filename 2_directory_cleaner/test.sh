echo "current working directory is $(pwd)"
rm -rf test_dir
cp -r ../test_dir_template test_dir
./dirclean ./test_dir
ls ./test_dir
