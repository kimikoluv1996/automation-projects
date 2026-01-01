rm -rf test_dir
cp -r test_dir_template test_dir
python main.py --dry-run test_dir
python main.py test_dir