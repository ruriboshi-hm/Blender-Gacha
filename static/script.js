const singleButton = document.getElementById("singleButton");
const tenButton = document.getElementById("tenButton");
const cardArea = document.getElementById("cardArea");
const modal = document.getElementById("imageModal");
const modalImage = document.getElementById("modalImage");

async function drawGacha(count) {
    
    const response = await fetch(`/gacha?count=${count}`);
    const data = await response.json();

    cardArea.innerHTML = "";

    data.forEach((item,index) => {
        
        const card =document.createElement("div");
        card.className = "card";

        card.innerHTML = `
        <div class="card-inner">
            <div class="card-front">
                <img src="/static/images/card-front.jpg" />
            </div>

            <div class="card-back ${item.rarity}">
                <div class="carousel">
                    <img src=${item.image[0]} class="card-image"/>

                    <div class="buttons">
                        <button class="prev">◀</button>
                        <button class="next">▶</button>
                    </div>
                </div>

                <h3>${item.rarity} ${item.name}</h3>
                <p>${item.about}</p>
            </div>
        </div>
        `;

        cardArea.appendChild(card);

        card.querySelector(".next").addEventListener("click",(e)=>{
            e.stopPropagation();

            let img = card.querySelector(".card-image");
            let index = parseInt(img.dataset.index || 0);

            index = (index + 1) % item.image.length;

            img.src = `${item.image[index]}`;
            img.dataset.index = index;
        });

        card.querySelector(".prev").addEventListener("click",(e)=>{
            e.stopPropagation();

            let img = card.querySelector(".card-image");
            let index = parseInt(img.dataset.index || 0);

            index = (index - 1 + item.image.length) % item.image.length;

            img.src = `${item.image[index]}`;
            img.dataset.index = index;
        });

        setTimeout(()=>{
            card.classList.add("flipped");
        },500 + index*500);
    });
}

singleButton.addEventListener("click",()=>drawGacha(1))
tenButton.addEventListener("click",()=>drawGacha(10));

document.addEventListener("click", (e)=>{
    if (e.target.classList.contains("card-image")){
        modalImage.src = e.target.src;
        modal.style.display = "flex";
    }
});

modal.addEventListener("click",()=>{
    modal.style.display = "none";
});