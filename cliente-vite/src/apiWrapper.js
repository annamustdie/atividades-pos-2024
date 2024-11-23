const BASE_URL = "https://jsonplaceholder.typicode.com/users";

export async function listarUsuarios() {
    try {
        const response = await fetch(BASE_URL);
        if (!response.ok) throw new Error(`Erro: ${response.status}`);
        return await response.json();
    } catch (error) {
        console.error("Erro ao listar usuários:", error);
        return [];
    }
}

export async function criarUsuario(nome, username, email) {
    try {
        const response = await fetch(BASE_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ name: nome, username, email }),
        });
        if (!response.ok) throw new Error(`Erro: ${response.status}`);
        return await response.json();
    } catch (error) {
        console.error("Erro ao criar usuário:", error);
        return null;
    }
}
