class Chain {
  constructor(nodes, speed, end) {
    this.nodes = nodes; // ノード配列 {x, y, size, updateRelative()}
    this.speed = speed; // 移動スピード
    this.end = end;     // 終端 {x, y}
  }

  moveTo(x, y) {
    // 先頭ノードの状態を更新
    this.nodes[0].updateRelative(true, true);

    // 終点との距離を計算
    let dist = ((x - this.end.x) ** 2 + (y - this.end.y) ** 2) ** 0.5;
    let len = Math.max(0, dist - this.speed);

    // 後ろから順にノードを追従させる
    for (let i = this.nodes.length - 1; i >= 0; i--) {
      let node = this.nodes[i];
      let ang = Math.atan2(node.y - y, node.x - x);
      node.x = x + len * Math.cos(ang);
      node.y = y + len * Math.sin(ang);
      x = node.x;
      y = node.y;
      len = node.size;
    }
  }

  update() {
    // マウス位置に追従
    this.moveTo(Input.mouse.x, Input.mouse.y);
  }
}
// main.js - シンプルなチェイン実装 + マウス追従表示

// // Input: マウス位置を保持
// const Input = { mouse: { x: 0, y: 0 } };

// // 初期セットアップ（canvas）
// const canvas = document.getElementById('canvas');
// const ctx = canvas.getContext('2d');

// function resize() {
//   // 実際のピクセルサイズを合わせる
//   const dpr = window.devicePixelRatio || 1;
//   canvas.width = Math.floor(canvas.clientWidth * dpr);
//   canvas.height = Math.floor(canvas.clientHeight * dpr);
//   ctx.setTransform(dpr,0,0,dpr,0,0);
// }
// window.addEventListener('resize', resize);
// resize();

// canvas.addEventListener('mousemove', (e) => {
//   const rect = canvas.getBoundingClientRect();
//   // マウス座標（CSSピクセル）
//   Input.mouse.x = e.clientX - rect.left;
//   Input.mouse.y = e.clientY - rect.top;
// });

// // Node のテンプレート
// class Node {
//   constructor(x, y, size = 16) {
//     this.x = x;
//     this.y = y;
//     this.size = size; // 次ノードへ渡す「長さ」的なもの
//   }
//   updateRelative() {
//     // ここは将来拡張するためのプレースホルダ
//   }
// }

// // Chain クラス（あなたのロジックを整えた版）
// class Chain {
//   constructor(nodes, speed = 8, end = { x: 0, y: 0 }) {
//     this.nodes = nodes;
//     this.speed = speed;
//     this.end = end;
//   }

//   moveTo(x, y) {
//     // 先頭ノードの状態更新（元コードの意図を引き継ぐ）
//     if (this.nodes[0] && typeof this.nodes[0].updateRelative === 'function') {
//       this.nodes[0].updateRelative(true, true);
//     }

//     // 終点（this.end）との距離を計算して「len」を求める
//     let dist = Math.hypot(x - this.end.x, y - this.end.y);
//     // 末端が目標へ移動する際の補正（元コードの dist - speed 的な挙動）
//     let len = Math.max(0, dist - this.speed);

//     // 後ろから前へノードを詰める（鎖の追従）
//     for (let i = this.nodes.length - 1; i >= 0; i--) {
//       const node = this.nodes[i];
//       // 角度は node -> (x,y) の方向（ノードが (x,y) に向かう）
//       const ang = Math.atan2(node.y - y, node.x - x);
//       node.x = x + len * Math.cos(ang);
//       node.y = y + len * Math.sin(ang);

//       // 次のループでは基準点をこのノードにし、長さを node.size にする
//       x = node.x;
//       y = node.y;
//       len = node.size;
//     }
//   }

//   update() {
//     this.moveTo(Input.mouse.x, Input.mouse.y);
//   }

//   draw(ctx) {
//     // 線でつなぐ
//     ctx.beginPath();
//     for (let i = 0; i < this.nodes.length; i++) {
//       const n = this.nodes[i];
//       if (i === 0) ctx.moveTo(n.x, n.y);
//       else ctx.lineTo(n.x, n.y);
//     }
//     ctx.strokeStyle = 'rgba(255,255,255,0.9)';
//     ctx.lineWidth = 2;
//     ctx.stroke();

//     // ノードを丸で描画
//     for (let n of this.nodes) {
//       ctx.beginPath();
//       ctx.arc(n.x, n.y, Math.max(2, n.size/4), 0, Math.PI * 2);
//       ctx.fillStyle = 'rgba(255,165,0,0.95)';
//       ctx.fill();
//     }
//   }
// }

// // 初期ノード群を生成
// function makeChain(x, y, count = 10) {
//   const nodes = [];
//   for (let i = 0; i < count; i++) {
//     // 最初は少し斜めに並べておく
//     nodes.push(new Node(x - i * 16, y, 16));
//   }
//   return nodes;
// }

// const chain = new Chain(makeChain(200, 200, 14), 10, { x: 400, y: 300 });

// // アニメーションループ
// function loop() {
//   // クリア
//   ctx.clearRect(0, 0, canvas.width, canvas.height);

//   // 更新・描画
//   chain.update();
//   chain.draw(ctx);

//   requestAnimationFrame(loop);
// }
// requestAnimationFrame(loop);

// // マウスがキャンバス外の時は中央へ
// canvas.addEventListener('mouseleave', () => {
//   Input.mouse.x = canvas.clientWidth / 2;
//   Input.mouse.y = canvas.clientHeight / 2;
// });
