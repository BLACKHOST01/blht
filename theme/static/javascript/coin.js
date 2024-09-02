
//     const coinId = "{{ coin.id }}";
//     const socket = new WebSocket(`ws://${window.location.host}/ws/crypto/${coinId}/`);




//     const currentPrice = {{ coin.current_price }};

//     function convertCoinToUSD() {
//         const coinAmount = document.getElementById('coinAmount').value;
//         const usdAmount = (coinAmount * currentPrice).toFixed(2);
//         document.getElementById('usdAmount').textContent = `$${usdAmount}`;
//     }

//     function convertUSDToCoin() {
//         const usdAmount = document.getElementById('usdAmount').value;
//         const coinAmount = (usdAmount / currentPrice).toFixed(8);
//         document.getElementById('coinAmount').textContent = `${coinAmount} {{ coin.symbol }}`;
//     }

//     document.getElementById('coinAmount').addEventListener('input', convertCoinToUSD);
//     document.getElementById('usdAmount').addEventListener('input', convertUSDToCoin);


//     function updateElement(elementId, newValue, oldValue) {
//         const element = document.getElementById(elementId);
//         if (newValue > oldValue) {
//             element.classList.remove('text-red-500');
//             element.classList.add('text-green-500');
//         } else if (newValue < oldValue) {
//             element.classList.remove('text-green-500');
//             element.classList.add('text-red-500');
//         }
//         element.textContent = newValue;
//     }

//     socket.onmessage = function(event) {
//         const data = JSON.parse(event.data);
//         updateElement('current-price', `$${data.current_price.toFixed(2)}`, parseFloat(document.getElementById('current-price').textContent.slice(1)));
//         updateElement('market-cap', `$${data.market_cap.toLocaleString()}`, parseFloat(document.getElementById('market-cap').textContent.slice(1).replace(/,/g, '')));
//         updateElement('volume-24h', `$${data.volume_24h.toLocaleString()}`, parseFloat(document.getElementById('volume-24h').textContent.slice(1).replace(/,/g, '')));
//         updateElement('circulating-supply', `${data.circulating_supply.toLocaleString()} ${data.symbol}`, parseFloat(document.getElementById('circulating-supply').textContent.split(' ')[0].replace(/,/g, '')));
//         updateElement('change-1h', `${data.price_change_percentage_1h.toFixed(2)}%`, parseFloat(document.getElementById('change-1h').textContent));
//         updateElement('change-24h', `${data.price_change_percentage_24h.toFixed(2)}%`, parseFloat(document.getElementById('change-24h').textContent));
//         updateElement('change-7d', `${data.price_change_percentage_7d.toFixed(2)}%`, parseFloat(document.getElementById('change-7d').textContent));
//         updateElement('ath', `$${data.ath.toFixed(2)}`, parseFloat(document.getElementById('ath').textContent.slice(1)));
//         zupdateElement('ath-change-percentage', `${data.ath_change_percentage.toFixed(2)}%`, parseFloat(document.getElementById('ath-change-percentage').textContent));
//         currentPrice = data.current_price;
//         convertCoinToUSD();
//         convertUSDToCoin();
//    };