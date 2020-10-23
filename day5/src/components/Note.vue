<template>
    <div>
        <h4>留言板</h4>
        <input type="text" v-model="note">
        <button @click="addNote">添加留言</button>

        <ul>
            <li v-for="(note, index) in notes" :key="index">
                <span>{{note}}</span>
                <button @click="remove(index)">删除</button>
            </li>
        </ul>

        <span>留言总数量：{{notes.length}}条</span>
        <br><br>
        <button v-show="flag" @click="remove_all(0, notes.length)">删除所有</button>
    </div>
</template>

<script>
export default {
    name: "Note",
    data:function () {
        return {
            note: "",
            notes: localStorage.notes ? JSON.parse(localStorage.notes) : [],
            flag: true,
        }
    },
    methods: {
        addNote() {
            let note = this.note;
            if (note){
                this.notes.push(this.note);
                localStorage.notes = JSON.stringify(this.notes);
                this.note = "";
                this.flag = true;
            }
        },
        remove(index) {
            this.notes.splice(index, 1)
            localStorage.notes = JSON.stringify(this.notes);
            if (!this.notes.length){
                this.flag = false;
                localStorage.removeItem("notes");
            }
        },
        remove_all(index, num){
            this.notes.splice(index, num);
            localStorage.removeItem("notes");
            this.flag = false;
        }
    },
    created: function () {
        let notes = this.notes;
        if (!notes.length) {
            this.flag = false;
        }
    },
}
</script>

<style scoped>

</style>
