SITEDIR=$(python -m site --user-site)
mkdir -p "$SITEDIR"
echo $(pwd)" > "$SITEDIR/bot2pix.pth"
