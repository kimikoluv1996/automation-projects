echo "current working directory is $(pwd)"
rm -rf test_dir
cp -r ../test_dir_template test_dir
#python3 main.py --dry-run test_dir
python3 main.py ./test_dir