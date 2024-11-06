-- レーダーtsukurounokai8,17
-- レーダーid,最大角度設定
local radarid = 1 -- レーダーid
-- ↑    id変更8,20　--確認
local minAngle = -90
local maxAngle = 90

function onTick()
    -- レーダー入力取得
    -- local input1 = input.getNumber
    local input1 = input.getNumber(1) -- -1から1の値を取得
    --local angle = minAngle + (input1)
    local angle = minAngle + (input1 * (maxAngle - minAngle)) -- -90度から90度に8.19

    -- レーダーの角度を設定
    radar.setRotation(radarid, angle)
    -- 何ここ

    -- レーダーで対象物をスキャン
    local target = radar.getTarget(radarid)
    if target then
        -- 対象物の位置座標取得
        local targetX = target.x
        local targetY = target.y
        local targetZ = target.z
        -- 対象物の方向を計算     
        local targetAngle = math.atan2(targetY, targetX) * (180 / math.pi) -- ラジアンを度に変換
        -- 対象物の方向へ装置の回転
        output.setNumber(1, targetAngle) -- 必要に応じて出力番号を変更
        -- 8.20
    end-- 書き忘れてる8.21
end