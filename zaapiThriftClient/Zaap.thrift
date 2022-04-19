namespace py zaap

service Zaapi {
    void connect(1:string gameName, 2:string releaseName, 3:i32 instanceId, 4:string hash),
    void auth_getGameToken(1:string gameSession, 2:i32 gameId),
}
