package exo3;

public class PrePersist extends Event {

	public PrePersist() {
		super("prePersist");
	}

	public void traiter(EventInterceptor ei, Object entity){
		ei.prePersist(entity);
	}

}
