const singleButton = document.getElementById("singleButton");
const tenButton = document.getElementById("tenButton");
const cardArea = document.getElementById("cardArea");

async function drawGacha(count) {
    
    const response = await fetch(`/gacha?count=${count}`);
    const data = await response.json();

    cardArea.innerHTML = "";

    data.forEach((item,index) => {
        
        const card =document.createElement("div");
        card.className = "card";

        card.innerHTML = `
        <div class="card-inner">
            <div class="card-front"><img src="/static/images/card-front.jpg" /></div>
            <div class="card-back ${item.rarity}"><img src=${item.image} /><h3>${item.rarity} ${item.name}</h3>${item.about}</div>
        </div>
        `;

        cardArea.appendChild(card);

        setTimeout(()=>{
            card.classList.add("flipped");
        },500 + index*500);
    });
}

singleButton.addEventListener("click",()=>drawGacha(1))
tenButton.addEventListener("click",()=>drawGacha(10));