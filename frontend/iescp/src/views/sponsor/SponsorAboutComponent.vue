<template>
    <div>
        <SponsorNavbar />
        <div class="container about-content">
            <h1>About Us</h1>
            <p>
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Ex culpa itaque facilis cumque eaque? Eos labore repellat voluptatem consequatur reiciendis fuga, reprehenderit impedit ad? Ullam nam sint doloribus similique illum earum praesentium explicabo dolores maiores aperiam? Necessitatibus, quod laboriosam officia facere magni vel recusandae aperiam, provident quam ullam, facilis minima.
            </p>
            <p>
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestias, maiores mollitia, aut reprehenderit atque amet accusamus ea perspiciatis, nihil magni incidunt fugiat possimus exercitationem tenetur ipsa unde quod animi non fuga quas laudantium. Quaerat error impedit, quod omnis totam eveniet placeat ipsa sint labore sit rerum officiis quo libero dolorum.
            </p>
            <p>
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde blanditiis beatae necessitatibus, nisi officia minima eaque vel aperiam tempora ut mollitia natus exercitationem. Beatae praesentium molestiae quod consectetur mollitia necessitatibus suscipit. Doloremque placeat similique eaque! A, odit quos itaque consectetur voluptas ipsam ad saepe, beatae nostrum ut qui eum quisquam perspiciatis aliquid, deserunt doloremque. Fuga officiis at maiores cumque quia deserunt dolore aperiam tenetur id, est, sit eveniet accusantium.
            </p>
            <p>
                Lorem ipsum dolor sit, amet consectetur adipisicing elit. Nulla natus, delectus aliquam quos quaerat voluptatem nobis nesciunt molestias, nisi voluptas excepturi veritatis dolore voluptate error enim autem dolorum. Corrupti dicta quae sint atque, doloremque vitae debitis iusto porro assumenda consectetur, possimus modi inventore eveniet repellendus dolore! Qui quas maxime impedit, expedita quia, fuga atque soluta ratione dolorem excepturi sunt nemo voluptate? Porro expedita tenetur officiis alias quaerat sint dolorem sunt hic accusamus.
            </p>
        </div>
    </div>
</template>

<script>
import SponsorNavbar from '@/components/sponsor/SponsorNavbar.vue';

export default {
    components: {
        SponsorNavbar
    }
};
</script>

<style scoped>
.about-content {
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 8px;
    margin-top: 20px;
}

.about-content h1 {
    color: #333;
    margin-bottom: 20px;
}

.about-content p {
    color: #555;
    line-height: 1.6;
    margin-bottom: 15px;
}
</style>
