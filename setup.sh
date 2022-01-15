SITEDIR=$(python -m site --user-site)
echo $SITEDIR
mkdir -p "$SITEDIR"
echo $(pwd)"/src" > "$SITEDIR/bot2pix.pth"
